# EST 4 Web Estimator — Deployment Guide

## What You Need
1. An **Anthropic API key** (get one at https://console.anthropic.com — costs ~$5-20/month in usage)
2. A **Railway account** (free to start, ~$5/month for always-on) at https://railway.app
3. Your domain (optional — add later)

---

## Deploy to Railway (Recommended — Simplest)

### Step 1 — Push to GitHub
1. Create a free GitHub account at https://github.com if you don't have one
2. Create a new repository called `est4-app`
3. Upload all files from the `EST4_App/` folder to the repository

### Step 2 — Deploy on Railway
1. Go to https://railway.app and sign in with GitHub
2. Click **New Project → Deploy from GitHub repo**
3. Select your `est4-app` repository
4. Railway auto-detects it's a Python app

### Step 3 — Set Environment Variables
In Railway dashboard → your project → **Variables** tab, add:
```
ANTHROPIC_API_KEY = sk-ant-YOUR-KEY-HERE
SECRET_KEY        = any-long-random-string-you-make-up
```

### Step 4 — Get Your URL
Railway gives you a URL like `est4-app.railway.app` — that's your live app!

### Step 5 — Add Your Domain (Optional)
In Railway → your project → **Settings → Domains**:
- Add your custom domain (e.g., `estimate.yourdomain.com`)
- Update your domain's DNS to point to Railway (they'll give you the CNAME)

---

## Running Locally (for testing)

```bash
cd EST4_App
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
python app.py
```

Then open http://localhost:5000 in your browser.

---

## Cost Breakdown

| Item | Cost |
|------|------|
| Railway hosting | ~$5/month |
| Anthropic API per estimate | ~$0.05–0.25 per job |
| Custom domain | ~$15/year |
| **Total to run** | **~$5-10/month** |

At 10 paid subscribers ($1,800/month each) → **$18,000/month revenue vs ~$10 cost**

---

## Adding Stripe Payments (Phase 2)

When you're ready to charge real money:
1. Create a Stripe account at https://stripe.com
2. The payment hooks are already marked in `app.py` (search for "Stripe")
3. Contact a developer or come back to EST 4 for help integrating

---

## Support
Built by EST 4. Questions? jaysozkesen@gmail.com
