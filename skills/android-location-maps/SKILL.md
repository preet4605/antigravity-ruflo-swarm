---
name: android-location-maps
description: "Google Maps SDK, FusedLocationProvider, and Background GeoFencing."
category: hardware-form-factors
risk: medium
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@maps"
    - "location"
    - "geofence"
---

# Location Services & Maps Integration 🌍

Location is sensitive data. Apps must gracefully handle denial of permissions and battery-friendly location polling.

## ⚡ When to Use
- When drawing maps, plotting markers, or grabbing user coordinates.

## 🏗️ Core Rules / Pillars

### 1. Fused Location Provider
- **Pattern**: Directly calling `LocationManager` is an outdated anti-pattern.
- **Implementation**: ALWAYS use `FusedLocationProviderClient` from Google Play Services, which intelligently coalesces GPS, Wi-Fi, and Cell signals to save battery.

### 2. Compose Maps
- **Pattern**: Use the official Google Maps Compose library (`com.google.maps.android:maps-compose`).
- **Implementation**:
  ```kotlin
  val cameraPositionState = rememberCameraPositionState {
      position = CameraPosition.fromLatLngZoom(singapore, 10f)
  }
  GoogleMap(
      modifier = Modifier.fillMaxSize(),
      cameraPositionState = cameraPositionState
  ) {
      Marker(
          state = MarkerState(position = singapore),
          title = "Singapore",
          snippet = "Marker in Singapore"
      )
  }
  ```

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Do not ask for `ACCESS_BACKGROUND_LOCATION` up front. Android explicitly rejects apps that do this. You must ask for Foreground location first, explain the need, and only then ask the user to elevate to Background location.
