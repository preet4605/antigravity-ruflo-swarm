---
name: android-bluetooth-ble
description: "Handling Bluetooth Low Energy, flow wrappers, and Android 12+ permissions."
category: hardware-form-factors
risk: high
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@ble"
    - "bluetooth"
    - "iot"
---

# Android Bluetooth Low Energy (BLE) & Permissions 📡

Working with IoT devices, Gatt Servers, and BLE scanning requires precise lifecycle control and permission handling.

## ⚡ When to Use
- When connecting to hardware devices via Bluetooth.

## 🏗️ Core Rules / Pillars

### 1. The Android 12+ Permission Shift
- **Pattern**: Location permissions are NO LONGER explicitly required for BLE *if* you declare that you are not using BLE for location tracking.
- **Implementation**: Use `BLUETOOTH_CONNECT` and `BLUETOOTH_SCAN` permissions in the manifest, and optionally set `android:usesPermissionFlags="neverForLocation"` on `BLUETOOTH_SCAN`.

### 2. Reactive BLE Wrappers
- **Pattern**: The native `BluetoothGattCallback` is entirely callback-based and prone to race conditions if used directly.
- **Implementation**: You MUST wrap BLE reads, writes, and connection states in Kotlin `callbackFlow { }` or `MutableStateFlow` to guarantee state correctness across coroutines.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: NEVER fire multiple BLE GATT operations at exactly the same time. The Android BLE stack will drop packets quietly. Always queue GATT operations sequentially!
