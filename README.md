# 🧑‍🍳 Emoji Kitchen Web App

This web application allows users to browse and combine emojis using Google's Emoji Kitchen. Users can select two emojis and see their unique combination, showcasing the creative illustrations from the Emoji Kitchen project.

## Features

- Browse and search through a comprehensive list of emojis
- Select two emojis to combine
- View the unique combination created by Emoji Kitchen
- Responsive design for various screen sizes

## Getting Started

### Prerequisites

- Node.js (version 14 or later)
- npm (comes with Node.js)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/emoji-kitchen-webapp.git
   cd emoji-kitchen-webapp
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Download the metadata file:
   ```
   curl -L --compressed https://raw.githubusercontent.com/xsalazar/emoji-kitchen-backend/main/app/metadata.json -o src/metadata.json
   ```

4. Start the development server:
   ```
   npm run dev
   ```

5. Open your browser and visit `http://localhost:5173` to see the app running.

## Building for Production

To create a production build, run:

```
npm run build
```

The built files will be in the `dist/` directory.

## Deployment

This project is set up to automatically deploy to GitHub Pages when changes are pushed to the `main` branch. The deployment is handled by the GitHub Actions workflow defined in `.github/workflows/deploy.yml`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Google's Emoji Kitchen for providing the emoji combinations
- The original [Emoji Kitchen website](https://emojikitchen.dev/) for inspiration
