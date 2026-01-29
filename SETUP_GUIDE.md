# Action Repo Setup Guide

## Quick Start Guide

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `action-repo`
3. Description: "Repository to trigger webhook events for TechStax assignment"
4. Choose **Public** or **Private**
5. **DO NOT** check "Initialize this repository with a README"
6. Click **Create repository**

### Step 2: Push This Code to GitHub

Open PowerShell/Terminal in this folder and run:

```bash
cd "c:\Users\laksh\OneDrive\Desktop\Assignment_Task\action-repo-main"

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Action repo for webhook testing"

# Rename branch to main
git branch -M main

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/action-repo.git

# Push to GitHub
git push -u origin main
```

**Important**: Replace `YOUR_USERNAME` with your actual GitHub username!

### Step 3: Configure GitHub Webhook

1. Go to your `action-repo` repository on GitHub
2. Click **Settings** (top menu)
3. Click **Webhooks** (left sidebar)
4. Click **Add webhook** button
5. Fill in the form:
   - **Payload URL**: `https://webhook-repo-3.onrender.com/webhook/receiver`
   - **Content type**: Select `application/json`
   - **Secret**: Leave empty (or add one if you configured it in Render)
   - **Which events would you like to trigger this webhook?**
     - Click **"Let me select individual events"**
     - ✅ Check **"Pushes"**
     - ✅ Check **"Pull requests"**
   - **Active**: ✅ Make sure this is checked
6. Click **Add webhook**

### Step 4: Test the Webhook

#### Test Push Event:

```bash
# Make a small change
echo "Test push" >> test.txt
git add test.txt
git commit -m "Test: Trigger push webhook"
git push origin main
```

Then check: https://webhook-repo-3.onrender.com/

You should see: `{your-username} pushed to main on {timestamp}`

#### Test Pull Request Event:

```bash
# Create a new branch
git checkout -b feature-test

# Make changes
echo "Feature code" >> feature.txt
git add feature.txt
git commit -m "Add feature"
git push origin feature-test
```

Then on GitHub:
1. Go to your repository
2. Click **Pull requests** → **New pull request**
3. Select `feature-test` → `main`
4. Click **Create pull request**

Check dashboard - should show PR event.

#### Test Merge Event:

1. On the PR page, click **Merge pull request**
2. Confirm merge

Check dashboard - should show MERGE event.

## Troubleshooting

### Webhook not triggering?

1. Check GitHub webhook delivery logs:
   - Go to **Settings → Webhooks** in your repo
   - Click on your webhook
   - Check **Recent Deliveries** tab
   - Look for any red ❌ errors

2. Verify Render URL is correct:
   - Make sure it's: `https://webhook-repo-3.onrender.com/webhook/receiver`
   - Test by opening: `https://webhook-repo-3.onrender.com/` (should show dashboard)

3. Check MongoDB connection:
   - Make sure MongoDB Atlas IP Access List includes `0.0.0.0/0` or Render IPs
   - Verify `MONGO_URI` is set correctly in Render environment variables

### Events not showing on dashboard?

1. Check Render logs:
   - Go to Render dashboard → Your service → **Logs**
   - Look for any MongoDB connection errors

2. Verify MongoDB:
   - Events are stored in `github_webhooks` database
   - Collection: `events`
   - Check MongoDB Atlas to see if events are being stored

## Assignment Submission Checklist

- [ ] `action-repo` created and pushed to GitHub
- [ ] GitHub webhook configured correctly
- [ ] Push event tested and visible on dashboard
- [ ] Pull request event tested and visible on dashboard
- [ ] Merge event tested and visible on dashboard
- [ ] Both repository URLs ready for submission:
  - `action-repo`: https://github.com/YOUR_USERNAME/action-repo
  - `webhook-repo`: https://github.com/YOUR_USERNAME/webhook_repo
- [ ] Dashboard URL: https://webhook-repo-3.onrender.com/

---

**Good luck with your assignment! 🚀**
