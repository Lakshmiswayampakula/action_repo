# Quick Test Commands

Copy and paste these commands to quickly test webhook events:

## Test Push Event

```bash
cd "c:\Users\laksh\OneDrive\Desktop\Assignment_Task\action-repo-main"
echo "Test push $(Get-Date)" >> test.txt
git add test.txt
git commit -m "Test: Trigger push webhook"
git push origin main
```

Then check: https://webhook-repo-3.onrender.com/

---

## Test Pull Request Event

```bash
cd "c:\Users\laksh\OneDrive\Desktop\Assignment_Task\action-repo-main"
git checkout -b pr-test-$(Get-Date -Format "yyyyMMdd-HHmmss")
echo "PR test content" >> pr-test.txt
git add pr-test.txt
git commit -m "Test: Create PR"
git push origin HEAD
```

Then on GitHub:
1. Go to your repo → **Pull requests** → **New pull request**
2. Select your new branch → `main`
3. Click **Create pull request**

Check dashboard for PR event.

---

## Test Merge Event

After creating PR above:
1. Go to the PR page
2. Click **Merge pull request**
3. Confirm merge

Check dashboard for MERGE event.

---

## Verify All Events

Open: https://webhook-repo-3.onrender.com/

You should see all three event types:
- ✅ PUSH
- ✅ PULL_REQUEST  
- ✅ MERGE
