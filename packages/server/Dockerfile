FROM node:20-slim

WORKDIR /app

COPY package.json pnpm-workspace.yaml ./
COPY packages ./packages

RUN corepack enable && corepack prepare pnpm@9.0.0 --activate
RUN pnpm -w install --frozen-lockfile=false
RUN pnpm -C packages/server build

EXPOSE 8787
CMD ["node", "packages/server/dist/index.js"]
