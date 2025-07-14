# AWS S3 Static Website Deployment

This repository contains static website files for deploying a simple HTML/CSS website on AWS S3.

## 📁 Files
- `index.html` - Main static page
- `style.css` - Styling for the webpage

## 🚀 How to Use
1. Enable static website hosting on your S3 bucket
2. Upload the files
3. Set `index.html` as your index document

---

## 📁 Project Structure

```
.
├── index.html         # Static website content
├── default.conf       # NGINX server config
├── Dockerfile         # Docker image definition
└── .github/
    └── workflows/
        └── docker-publish.yml  # CI/CD workflow
```

---

## 🐳 Docker

### 🔧 Build Locally

```bash
docker build -t yourname/static-nginx .
```

### ▶️ Run Container

```bash
docker run -d -p 8080:80 yourname/static-nginx
```
Visit: [http://localhost:8080](http://localhost:8080)

---

## 🚀 CI/CD with GitHub Actions

This repository includes a GitHub Actions workflow (`.github/workflows/docker-publish.yml`) that builds and (optionally) pushes your Docker image on each commit.

---

## 📝 Customization

- Edit `index.html` to update your site’s content.
- Edit `default.conf` to adjust NGINX settings.
- Modify `Dockerfile` for advanced Docker usage.
- Update `docker-publish.yml` to fit your preferred deployment pipeline.

---
