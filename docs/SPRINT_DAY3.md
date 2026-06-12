# Day 3 Sprint: Flutter Mobile App & Final Integration

## Objectives (8-10 hours)

✅ Complete Flutter UI screens (4 main screens)
✅ Implement camera and image picker
✅ Integrate with backend API
✅ Implement local database (SQLite)
✅ Build analytics graphs
✅ Create disease visualization features
✅ Deploy and test MVP

## Timeline

### Hour 0-1: Flutter Project Setup

```bash
cd flutter_app
flutter pub get
flutter pub upgrade
```

### Hour 1-3: Core Screens Structure

**Files to create:**

```
lib/
├── main.dart                      # App entry
├── screens/
│   ├── home_screen.dart          # Home/Scan screen
│   ├── history_screen.dart       # History screen
│   ├── analytics_screen.dart     # Analytics screen
│   ├── profile_screen.dart       # Profile screen
│   ├── scan_detail_screen.dart   # Scan details
│   └── login_screen.dart         # Login screen
├── widgets/
│   ├── disease_card.dart         # Disease card widget
│   ├── chart_widgets.dart        # Chart components
│   └── custom_widgets.dart       # Custom widgets
├── models/
│   ├── scan_model.dart           # Scan data model
│   ├── disease_model.dart        # Disease model
│   └── user_model.dart           # User model
├── services/
│   ├── api_service.dart          # API calls
│   ├── db_service.dart           # Local database
│   └── image_service.dart        # Image processing
├── providers/
│   ├── auth_provider.dart        # Auth state
│   ├── scan_provider.dart        # Scan state
│   └── analytics_provider.dart   # Analytics state
└── utils/
    ├── constants.dart            # Constants
    └── helpers.dart              # Helper functions
```

### Hour 3-5: Screen Implementation

#### 1. Home/Scan Screen (Hour 3-3.5)

```dart
// Features:
// - Camera button
// - Image picker button
// - Recent scan preview
// - Quick stats
// - Action buttons
```

#### 2. History Screen (Hour 3.5-4)

```dart
// Features:
// - List of past scans
// - Filter by disease
// - Search functionality
// - Tap to view details
// - Delete scan option
```

#### 3. Analytics Screen (Hour 4-4.5)

```dart
// Features:
// - Monthly graphs
// - Disease distribution pie chart
// - Health score chart
// - Severity level breakdown
// - Date range selector
```

#### 4. Profile Screen (Hour 4.5-5)

```dart
// Features:
// - User information
// - Farm details
// - Statistics
// - Settings
// - Logout button
```

### Hour 5-7: Backend Integration

**API Service Implementation:**

```dart
// app/services/api_service.dart

class ApiService {
  // Auth endpoints
  Future<LoginResponse> login(String email, String password)
  Future<RegisterResponse> register(UserData data)
  
  // Scan endpoints
  Future<ScanResult> predictDisease(File imageFile)
  Future<List<Scan>> getHistory(int page)
  Future<ScanDetail> getScanDetail(int scanId)
  
  // Analytics
  Future<Analytics> getMonthlyAnalytics(int month, int year)
  
  // User
  Future<UserProfile> getUserProfile()
  Future<void> updateProfile(UserData data)
}
```

### Hour 7-8: Local Database

**SQLite Integration:**

```dart
// app/services/db_service.dart

class DatabaseService {
  // Scan storage
  Future<void> saveScan(Scan scan)
  Future<List<Scan>> getAllScans()
  Future<Scan?> getScan(int id)
  Future<void> deleteScan(int id)
  
  // User data
  Future<void> saveUserProfile(UserProfile profile)
  Future<UserProfile?> getUserProfile()
  
  // Cache
  Future<void> cacheDiseaseInfo()
}
```

### Hour 8-10: Testing & Deployment

```bash
# Test on emulator
flutter run

# Test on physical device
flutter run -d <device_id>

# Build APK for Android
flutter build apk --release

# Build for iOS
flutter build ios --release
```

## Detailed Screen Implementations

### 1. Home Screen

```dart
class HomeScreen extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Leaf Disease Detection'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Camera/Image picker buttons
            Row(
              children: [
                FloatingActionButton(
                  onPressed: () => pickFromCamera(),
                  child: Icon(Icons.camera_alt),
                ),
                FloatingActionButton(
                  onPressed: () => pickFromGallery(),
                  child: Icon(Icons.image),
                ),
              ],
            ),
            // Recent scan preview
            RecentScanCard(),
            // Statistics
            StatsWidget(),
          ],
        ),
      ),
    );
  }
}
```

### 2. Scan Result Screen

```dart
class ScanResultScreen extends StatelessWidget {
  final ScanResult result;
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Scan Results')),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Disease name + confidence
            DiseaseTitleCard(result),
            
            // Image with visualization
            DiseaseVisualizationCard(result),
            
            // Disease info tabs
            DiseaseInfoTabs(result),
            
            // Recommendations
            RecommendationsSection(result),
            
            // Save button
            SaveScanButton(result),
          ],
        ),
      ),
    );
  }
}
```

### 3. Analytics Screen

```dart
class AnalyticsScreen extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final analytics = ref.watch(analyticsProvider);
    
    return Scaffold(
      body: analytics.when(
        data: (data) => SingleChildScrollView(
          child: Column(
            children: [
              // Health score chart
              LineChartWidget(data.monthlyScores),
              
              // Disease distribution
              PieChartWidget(data.diseaseDistribution),
              
              // Severity breakdown
              BarChartWidget(data.severityBreakdown),
              
              // Statistics
              StatisticsWidget(data),
            ],
          ),
        ),
        loading: () => Center(child: CircularProgressIndicator()),
        error: (err, stack) => ErrorWidget(error: err),
      ),
    );
  }
}
```

## Key Features Implementation

### 1. Camera Integration

```dart
Future<XFile?> pickFromCamera() async {
  final ImagePicker picker = ImagePicker();
  final XFile? photo = await picker.pickImage(
    source: ImageSource.camera,
    preferredCameraDevice: CameraDevice.rear,
  );
  return photo;
}
```

### 2. Image Upload & Prediction

```dart
Future<void> uploadAndPredict(File imageFile) async {
  final response = await apiService.predictDisease(imageFile);
  
  // Save to local DB
  await dbService.saveScan(response.scan);
  
  // Navigate to result screen
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (_) => ScanResultScreen(result: response),
    ),
  );
}
```

### 3. Chart Implementation

```dart
Widget buildMonthlyChart(List<MonthlyData> data) {
  return LineChart(
    LineChartData(
      gridData: FlGridData(show: true),
      titlesData: FlTitlesData(...),
      borderData: FlBorderData(...),
      lineBarsData: [
        LineChartBarData(
          spots: data.map((d) => FlSpot(d.month, d.score)).toList(),
          isCurved: true,
          color: Colors.green,
        ),
      ],
    ),
  );
}
```

## Deliverables at End of Day 3

✅ **Complete Flutter App**
   - 4 main screens implemented
   - Camera and image picker working
   - Real-time disease prediction
   - History and analytics
   - User profile management

✅ **Backend Integration**
   - All API calls working
   - JWT authentication
   - Image upload and processing
   - Data sync with server

✅ **Local Storage**
   - SQLite database configured
   - Scan history stored locally
   - User profile cached
   - Offline mode ready

✅ **MVP Features**
   - ✅ Capture/upload images
   - ✅ Disease detection
   - ✅ Visual localization
   - ✅ Disease information
   - ✅ Recommendations
   - ✅ History tracking
   - ✅ Monthly analytics
   - ✅ User profile

## Testing Checklist

- [ ] App launches successfully
- [ ] Login/Register working
- [ ] Camera capture working
- [ ] Image upload to backend successful
- [ ] Disease prediction returned
- [ ] Results displayed correctly
- [ ] History shows all scans
- [ ] Analytics graphs render
- [ ] Local storage working
- [ ] Offline mode functional

## Build & Release

### Android

```bash
flutter build apk --release
# Output: build/app/outputs/flutter-app-release.apk

# Or for Play Store
flutter build appbundle --release
# Output: build/app/outputs/bundle/release/app-release.aab
```

### iOS

```bash
flutter build ios --release
# Output: build/ios/iphoneos/Runner.app
```

## Performance Optimization

- Image compression before upload
- Model quantization (already TFLite)
- Lazy loading of images
- Pagination for history
- Local caching of API responses

## Next Steps (Post-MVP)

→ Community features
→ Weather integration
→ Push notifications
→ Offline ML inference
→ Multi-language support
→ App store publication

---

**Status:** 🎉 MVP Complete - Ready for Beta Testing!
