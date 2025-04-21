# Discourse-Saga: One Man vs SMTP

## 🧠 What This Is
This repo documents the full ride of setting up, breaking, and trying to resurrect a self-hosted Discourse forum — all in the name of learning how systems *really* work.

## ⚙️ Setup Timeline

### Phase 1: The Birth of the Forum
- Deployed Discourse using the official Docker method
- Started off using a **free DuckDNS domain**
- Got the site up and running — everything looked smooth

### Phase 2: The SMTP Reckoning
- Tried configuring SMTP with Mailgun for email functionality (registration, notifications, etc.)
- DuckDNS didn’t cut it — Mailgun wouldn’t verify domain or deliver emails properly
- Switched to a **paid custom domain** via Cloudflare: `micooolyet.com`
- Updated DNS, SPF, DKIM records — still had issues

### Phase 3: The Bootstrap Blues
- Discourse hit the dreaded bootstrap loop
- Docker containers kept restarting
- SMTP configs caused startup fails
- Attempted fixes:
  - Edited `app.yml` (probably 50+ times)
  - Switched SMTP ports, tested other mail services
  - Verified and re-verified domain configs
  - Sacrificed my sanity and sleep schedule

## 🔧 Lessons Learned
- Free domains are cool for testing, *not* for production setups needing email
- Email delivery is one of the most frustrating parts of self-hosting
- Always backup working configs
- Docker logs are your window into the underworld

## 🔜 Next Steps
- Re-deploy Discourse using the last working config and updated domain
- Try running mail config *before* full bootstrap
- Consider isolating mail testing with tools like `swaks`
- Document fixes, and win the SMTP war once and for all

---

> Started with DuckDNS. Got serious. Still debugging.

