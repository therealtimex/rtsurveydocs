# Stage 1 — Build
FROM node:20-alpine AS builder

WORKDIR /app

# Install dependencies
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy source
COPY . .

# Build English (no basePath)
RUN NODE_OPTIONS='--max-old-space-size=6144' yarn build

# Build all locales (one at a time to stay within memory)
RUN node scripts/build-split.mjs

# Merge English (out/) + locales (combined/*/) → dist/
RUN node scripts/merge-output.mjs


# Stage 2 — Serve
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
