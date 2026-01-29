# Action Repo

This repository is used to trigger GitHub Webhooks for testing a Flask-based webhook receiver.

## 🎯 Purpose

This repository serves as the **trigger repository** (`action-repo`) that sends webhook events to the webhook receiver application. When you perform actions in this repository (push, create pull request, merge), GitHub automatically sends webhook events to the configured endpoint.

## 📋 Supported Actions

This repository can trigger the following webhook events:

1. **PUSH** - When you push commits to any branch
2. **PULL_REQUEST** - When you create or update a pull request
3. **MERGE** - When you merge a pull request

## 🚀 Setup Instructions

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository named `action-repo`
2. **Do NOT initialize** with README, .gitignore, or license (we already have files)

### 2. Initialize and Push

```bash
cd "c:\Users\laksh\OneDrive\Desktop\Assignment_Task\action-repo-main"
git init
git add .
git commit -m "Initial commit: Action repo for webhook testing"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/action-repo.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Configure GitHub Webhook

1. Go to your `action-repo` repository on GitHub
2. Navigate to **Settings → Webhooks → Add webhook**
3. Configure the webhook:
   - **Payload URL**: `https://webhook-repo-3.onrender.com/webhook/receiver`
   - **Content type**: `application/json`
   - **Secret**: (optional, leave empty for now)
   - **Which events would you like to trigger this webhook?**
     - Select: **"Let me select individual events"**
     - ✅ Check **"Pushes"**
     - ✅ Check **"Pull requests"**
   - **Active**: ✅ Checked
4. Click **Add webhook**

## 🧪 Testing Webhook Events

### Test 1: PUSH Event

```bash
# Make a change to any file
echo "# Test commit" >> test.txt
git add test.txt
git commit -m "Test push event"
git push origin main
```

**Expected Result**: Check your webhook dashboard at `https://webhook-repo-3.onrender.com/` - you should see:
```
{your-username} pushed to main on {timestamp}
```

### Test 2: PULL_REQUEST Event

1. Create a new branch:
   ```bash
   git checkout -b feature-test
   ```

2. Make changes and commit:
   ```bash
   echo "Feature changes" >> feature.txt
   git add feature.txt
   git commit -m "Add feature"
   git push origin feature-test
   ```

3. On GitHub, create a Pull Request:
   - Go to your repository → **Pull requests → New pull request**
   - Select `feature-test` → `main`
   - Click **Create pull request**

**Expected Result**: Dashboard should show:
```
{your-username} submitted a pull request from feature-test to main on {timestamp}
```

### Test 3: MERGE Event

1. Merge the pull request you created in Test 2:
   - Go to the PR page
   - Click **Merge pull request**
   - Confirm merge

**Expected Result**: Dashboard should show:
```
{your-username} merged branch feature-test to main on {timestamp}
```

## 📁 Repository Structure

```
action-repo/
├── README.md          # This file
├── main.py            # Sample Python file
├── .gitignore         # Git ignore rules
└── test.txt           # Sample file for testing
```

## 🔗 Related Repositories

- **Webhook Receiver**: [webhook-repo](https://github.com/YOUR_USERNAME/webhook-repo)
- **Dashboard URL**: https://webhook-repo-3.onrender.com/

## 📝 Notes

- All webhook events are sent to: `https://webhook-repo-3.onrender.com/webhook/receiver`
- Events are stored in MongoDB and displayed on the dashboard
- Dashboard auto-refreshes every 15 seconds
- Make sure your MongoDB Atlas IP Access List allows connections from Render

## ✅ Assignment Checklist

- ✅ Repository created and pushed to GitHub
- ✅ GitHub webhook configured with correct endpoint
- ✅ Push events tested and working
- ✅ Pull request events tested and working
- ✅ Merge events tested and working
- ✅ All events visible on dashboard

---

**Created for TechStax Developer Assessment Task**
