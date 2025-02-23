# Use an official Node.js image as the base
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the entire frontend code
COPY . .

# Build the React app
RUN npm run build

# Serve the app using a lightweight web server
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]

# Expose port
EXPOSE 3000
