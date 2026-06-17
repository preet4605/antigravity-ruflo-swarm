---
name: android-google-workspace-expert
description: "Use when integrating Google Workspace APIs (Calendar, Drive, Docs) or implementing Google Sign-In with OAuth Scopes."
category: integrations
risk: high
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@google-workspace"
    - "google-calendar"
    - "google-drive"
    - "oauth-scopes"
    - "google-credentials"
    - "credential-manager"
---

# Google Workspace Integration Expert 📅🔐

A robust guideline for implementing Google Workspace APIs (Calendar, Drive) in modern Android applications using Android's Credential Manager and secure OAuth scopes.

## ⚡ When to Use
- **Google Sign-In**: Authenticating users securely.
- **Calendar Sync**: Reading/writing events to the user's Google Calendar.
- **Drive Backup**: Saving or restoring app data via Google Drive.

## 🔑 Rule 1: Modern Authentication (Credential Manager)
Google has deprecated legacy Google Sign-In (`GoogleSignInClient`). You **MUST** use Android's `CredentialManager` API for requesting permissions and access tokens.

### Scopes for Calendar
If an agent needs to add a Todo item to a calendar, request:
```kotlin
private val SCOPES = listOf("https://www.googleapis.com/auth/calendar.events")
```

## 📅 Rule 2: Google Calendar Integration 

**Anti-Pattern**: NEVER manually craft HTTP requests to `www.googleapis.com/calendar/v3/...`. This invites token expiration crashes and parsing errors.

**The Architect Standard:**
Use the official Google API Client Libraries for Android.
1. Add dependencies in `build.gradle.kts`:
   ```kotlin
   implementation("com.google.api-client:google-api-client-android:1.33.0")
   implementation("com.google.apis:google-api-services-calendar:v3-rev411-1.25.0")
   ```

2. Construct the Calendar Client securely:
   ```kotlin
   val credential = GoogleAccountCredential.usingOAuth2(context, listOf(CalendarScopes.CALENDAR_EVENTS))
   credential.selectedAccount = account.account // from CredentialManager

   val service = Calendar.Builder(
       com.google.api.client.extensions.android.http.AndroidHttp.newCompatibleTransport(),
       com.google.api.client.json.gson.GsonFactory.getDefaultInstance(),
       credential
   ).setApplicationName("TodoApp").build()
   ```

## 🔄 Rule 3: Background Sync via WorkManager
Never sync to Google Calendar on the main thread or directly from the UI layer. Ensure event-creation happens in the background.

```kotlin
class CalendarSyncWorker(context: Context, params: WorkerParameters) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result = withContext(Dispatchers.IO) {
        val todoId = inputData.getString("TODO_ID") ?: return@withContext Result.failure()
        
        try {
            val event = Event().apply {
                summary = "Complete Todo: $todoId"
                start = EventDateTime().setDateTime(DateTime(System.currentTimeMillis()))
                end = EventDateTime().setDateTime(DateTime(System.currentTimeMillis() + 3600000))
            }
            
            // service is injected
            service.events().insert("primary", event).execute()
            Result.success()
        } catch (e: Exception) {
            Result.retry() // WorkManager will automatically retry on network failure!
        }
    }
}
```

## 🛑 Common Hallucinations to Avoid
1. **API Keys**: Google Workspace APIs (Calendar/Drive) require **OAuth 2.0 Client IDs**, NOT restricted API Keys. 
2. **Intent Fallback**: If a user is not signed in to a Google Account, you cannot blindly fire the Calendar Client. You must intercept the `UserRecoverableAuthIOException` to re-prompt the user to sign in.
