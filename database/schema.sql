-- Create database
CREATE DATABASE IF NOT EXISTS leaf_disease_db;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    farm_location VARCHAR(255),
    farm_size FLOAT,
    crops_cultivated TEXT[] DEFAULT '{}',
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Diseases table
CREATE TABLE IF NOT EXISTS diseases (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    scientific_name VARCHAR(255),
    description TEXT,
    symptoms TEXT,
    causes TEXT,
    affected_crops TEXT[],
    image_url VARCHAR(500),
    research_links TEXT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Disease treatments
CREATE TABLE IF NOT EXISTS disease_treatments (
    id SERIAL PRIMARY KEY,
    disease_id INTEGER REFERENCES diseases(id) ON DELETE CASCADE,
    treatment_name VARCHAR(255),
    treatment_type VARCHAR(50), -- 'organic', 'chemical', 'prevention'
    description TEXT,
    application_method VARCHAR(255),
    frequency VARCHAR(100),
    cost_estimate FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fertilizer recommendations
CREATE TABLE IF NOT EXISTS fertilizers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    npk_ratio VARCHAR(20), -- e.g., "10:10:10"
    description TEXT,
    for_disease_id INTEGER REFERENCES diseases(id) ON DELETE SET NULL,
    recommended_quantity VARCHAR(100),
    frequency VARCHAR(100),
    cost_per_unit FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scans/Predictions
CREATE TABLE IF NOT EXISTS scans (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    image_path VARCHAR(500) NOT NULL,
    original_image_url VARCHAR(500),
    processed_image_url VARCHAR(500),
    disease_detected VARCHAR(255),
    confidence FLOAT,
    severity_level VARCHAR(50), -- 'mild', 'moderate', 'severe'
    affected_area_percentage FLOAT,
    localization_map_url VARCHAR(500),
    crop_type VARCHAR(100),
    scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scan disease details
CREATE TABLE IF NOT EXISTS scan_disease_details (
    id SERIAL PRIMARY KEY,
    scan_id INTEGER REFERENCES scans(id) ON DELETE CASCADE,
    disease_id INTEGER REFERENCES diseases(id),
    confidence_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scan recommendations
CREATE TABLE IF NOT EXISTS scan_recommendations (
    id SERIAL PRIMARY KEY,
    scan_id INTEGER REFERENCES scans(id) ON DELETE CASCADE,
    treatment_id INTEGER REFERENCES disease_treatments(id),
    fertilizer_id INTEGER REFERENCES fertilizers(id),
    priority INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User feedback
CREATE TABLE IF NOT EXISTS user_feedback (
    id SERIAL PRIMARY KEY,
    scan_id INTEGER REFERENCES scans(id) ON DELETE CASCADE,
    is_accurate BOOLEAN,
    feedback_text TEXT,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Analytics
CREATE TABLE IF NOT EXISTS monthly_analytics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    month DATE,
    total_scans INTEGER,
    diseases_detected TEXT[],
    most_common_disease VARCHAR(255),
    health_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_user_id ON scans(user_id);
CREATE INDEX idx_scan_date ON scans(scan_date);
CREATE INDEX idx_disease_name ON diseases(name);
CREATE INDEX idx_scan_disease ON scan_disease_details(scan_id);
