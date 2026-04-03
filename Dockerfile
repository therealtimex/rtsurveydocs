# Expects pre-built files in dist/ — run ./build.sh first
# docker compose build && docker compose up -d
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
