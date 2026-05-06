# Hardware Container Inventory - Offline PWA

A Progressive Web App for managing hardware container inventory that works completely offline on Android phones.

## Features

- ✅ Works offline after first visit
- ✅ Installable on Android home screen
- ✅ Fully responsive mobile design
- ✅ IndexedDB for local data storage
- ✅ Import/Export data as JSON
- ✅ Filter inventory by category and size
- ✅ Edit quantities and item details
- ✅ Quick decrement buttons (-1, -2, -4)

## Installation on Android

**⚠️ REQUIRES HTTPS:** The install prompt only works over HTTPS. See the Development section below for deployment options (GitHub Pages, Netlify, or ngrok).

### Method 1: Automatic Install Banner
1. Open the app in Chrome on your Android device (via HTTPS URL)
2. Look for the green "Install Now" banner at the top
3. Click "Install Now" and confirm

### Method 2: Chrome Menu
1. Open the app in Chrome on your Android device (via HTTPS URL)
2. Wait for the page to fully load
3. Tap the menu icon (three vertical dots) in the top right
4. Look for "Install app" or "Add to Home screen"
5. Tap it and confirm the installation

**Troubleshooting:**
- **Must use HTTPS** - `http://` won't work for PWA installation
- Make sure you're using **Chrome** browser (not Firefox or Samsung Internet)
- The page must be fully loaded before the install option appears
- Clear Chrome cache if you don't see the option: Settings > Privacy > Clear browsing data
- You may need to visit the page 2-3 times before Chrome offers installation
- Check that your device has enough storage space

### Method 3: Manual Add to Home Screen (Fallback)
If the install option doesn't appear:
1. Open Chrome menu (three dots)
2. Select "Add to Home screen"
3. Name it "Hardware" and tap "Add"

Note: This creates a shortcut but may not fully enable offline mode without HTTPS.

## Development

### IMPORTANT: HTTPS Required for PWA Installation

**PWAs require HTTPS to work on Android.** The local `http://` server won't trigger the install prompt on phones.

### Option 1: Deploy to Free HTTPS Hosting (Recommended)

The easiest way to use this app on your phone:

1. **GitHub Pages** (Free, permanent HTTPS hosting):
   - Create a GitHub account at github.com
   - Create a new repository (e.g., "hardware-inventory")
   - Upload all files (index.html, manifest.json, sw.js, icon-192.png, icon-512.png)
   - Go to Settings > Pages > Select "main" branch > Save
   - Access at `https://yourusername.github.io/hardware-inventory/`
   - The install prompt will appear on Android Chrome!

2. **Netlify/Vercel** (Even easier):
   - Drag and drop the Hardware folder
   - Get an instant HTTPS URL
   - Works immediately on Android

### Option 2: Use ngrok for Testing (Temporary HTTPS)

If you want to test locally with HTTPS:

1. **Download ngrok** from https://ngrok.com (free, no account needed for basic use)

2. **Start your local server:**
   ```bash
   python -m http.server 8080
   ```

3. **In another terminal, run ngrok:**
   ```bash
   ngrok http 8080
   ```

4. **Copy the HTTPS URL** (e.g., `https://abc123.ngrok.io`)

5. **Open that URL on your Android phone** - the install prompt will work!

### Option 3: Local Testing on PC Only

For testing on your PC (localhost works without HTTPS):

```bash
# Start server
python -m http.server 8080

# Or using Python 2
python -m SimpleHTTPServer 8080

# Then visit http://localhost:8080 in your browser
```

## Data Persistence

- All data is stored locally in IndexedDB
- **Persistent storage requested** - protects against automatic deletion when storage is low
- Data persists across sessions and app updates
- Export your data as JSON for backup
- Import JSON files to restore data

### Storage Protection

The app requests "persistent storage" from Chrome to prevent your data from being deleted when the device runs low on space. When you first use the app, Chrome may ask for permission to store data permanently - grant this to ensure your inventory is safe.

You can check storage status in the browser console (DevTools) where it shows:
- Whether persistent storage was granted
- How much storage you're using
- Available storage quota

## Browser Support

- Chrome/Edge (recommended for Android)
- Firefox
- Safari (iOS)

## Files

- `index.html` - Main application
- `manifest.json` - PWA manifest for installation
- `sw.js` - Service worker for offline functionality
