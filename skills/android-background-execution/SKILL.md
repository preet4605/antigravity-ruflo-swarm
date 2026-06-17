---
name: android-background-execution
description: Expert guidance on implementing and managing background tasks in modern Android applications (API 30+).
---

# Android Background Execution Skill

This skill provides a structured approach to implementing background work in Android, ensuring high performance, battery efficiency, and compliance with modern system restrictions (API 30 and above).

## When to Use

- Implementing deferred tasks (e.g., database sync, log uploading).
- Running immediate, user-perceivable tasks (e.g., media playback, active navigation).
- Scheduling time-sensitive actions (e.g., calendar reminders, exact alarms).
- Navigating background execution limits and battery optimization (Doze Mode).

## 🛠 Core Technologies

### 1. WorkManager (Recommended)

Use for **persistent, deferrable work** that must execute even if the app exits or the device restarts.

- **Immediate**: Tasks that should start as soon as possible (can use `setExpedited(true)`).
- **Long-Running**: Tasks that might run longer than 10 minutes (API 31+ requires a Foreground Service).
- **Periodic**: Recurring tasks (minimum 15-minute interval).

### 2. Foreground Services

Use for **immediate, user-visible work** that is the primary focus of the app (e.g., Music Player, Step Tracker).

- Must show a persistent notification.
- From API 34+, you must declare a `foregroundServiceType` in the manifest.

### 3. Alarms (`AlarmManager`)

Use for **exact, time-based scheduling**.

- Avoid for general background work to save battery.
- `setExactAndAllowWhileIdle()` is for high-precision needs (e.g., clocks).

---

## 🚀 Implementation Workflow

### 1. Choose the Right Tool

| Requirement | Recommended Tool |
| :--- | :--- |
| Deferrable, restart-resilient | `WorkManager` (OneTime/Periodic) |
| Immediate, continues when app is closed | `WorkManager` (Expedited) |
| User-visible, real-time | `Foreground Service` |
| Specific clock time (e.g. 8:00 AM) | `AlarmManager` |

### 2. Implementation Patterns

#### WorkManager (Kotlin)

```kotlin
class SyncWorker(context: Context, params: WorkerParameters) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        return try {
            // Background logic here
            Result.success()
        } catch (e: Exception) {
            if (runAttemptCount < 3) Result.retry() else Result.failure()
        }
    }
}
```

// Enqueueing

```kotlin
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.CONNECTED)
    .setRequiresBatteryNotLow(true)
    .build()

val syncRequest = OneTimeWorkRequestBuilder<SyncWorker>()
    .setConstraints(constraints)
    .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 1, TimeUnit.MINUTES)
    .build()

WorkManager.getInstance(context).enqueue(syncRequest)
```

#### Foreground Service (API 34+)

1. **Manifest Declaration**:

```xml
<service
    android:name=".MyService"
    android:foregroundServiceType="dataSync" />
```

2. **Service Implementation**:

```kotlin
class MyService : Service() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("Syncing Data")
            .setSmallIcon(R.drawable.ic_sync)
            .build()
        
        ServiceCompat.startForeground(this, 1, notification, FOREGROUND_SERVICE_TYPE_DATA_SYNC)
        // logic...
        return START_NOT_STICKY
    }
}
```

---

## 💡 Best Practices & Constraints

- **Battery Optimization**: Respect Doze Mode. `WorkManager` handles this automatically by batching requests.
- **Expedited Work**: For WorkManager tasks that need to start immediately, use `setExpedited(true)`. Note that this has quotas.
- **Connectivity**: Always use `Constraints` in `WorkManager` to prevent unnecessary wakeups when offline.
- **Error Handling**: Implement exponential backoff for retries to avoid "looping" failures.
- **Testing**: Use `WorkManagerTestInitHelper` for testing workers in unit/integration tests without waiting for real-world constraints.

## 📂 Project Organization

- Place Workers in `com.example.app.data.worker` or `com.example.app.ui.background`.
- Place Services in `com.example.app.service`.
- Keep business logic in `Repository` classes, not inside `Worker` or `Service` classes.
