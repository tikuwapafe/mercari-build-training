FROM node:20-alpine
WORKDIR /app

RUN addgroup -S mercari && adduser -S trainee -G mercari

COPY . .

RUN chown -R trainee:mercari /app

RUN npm ci

EXPOSE 3000

USER trainee

# Bind Vite servers to all network interfaces
CMD ["npm", "run", "start", "--", "--host"]
