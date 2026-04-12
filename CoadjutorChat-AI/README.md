# CoadjutorChat-AI — Chat UI

A modern, responsive AI chat interface built for the CampusPe Gen AI Assignment.

## Tech Stack
- HTML5 
- CSS3 
- Bootstrap 5.3
- jQuery 3.7
- Font Awesome 6.5
- Google Fonts (Inter, Fira Code)

## How to Run
1. Unzip the project folder
2. Open `index.html` in any modern browser (Chrome, Firefox, Safari, Edge)
3. No server or build step required — it's fully client-side

## Features Implemented
### Core (Tasks 1–4)
- Welcome screen with 4 suggestion cards in a grid
- Message bubbles: user (right, blue) vs AI (left, dark)
- Animated typing indicator with bouncing dots
- Auto-resizing textarea input
- Send button with enabled/disabled state
- Enter to send, Shift+Enter for new line
- Auto-scroll to latest message
- Sidebar (260px) with chat history and user profile
- Mobile-responsive with hamburger menu and slide-in sidebar

### Bonus Features
- 🌙 Dark/Light mode toggle with smooth transition
- 💬 Message formatting: **bold**, *italic*, `code`, ```code blocks```
- 📥 Export chat as `.txt` file using the Blob API
- 🖌 Custom scrollbar styling

## File Structure
```
YourName_ChatUI/
├── index.html          ← main entry point
├── css/
│   └── style.css       ← all custom styles
├── js/
│   └── chat.js         ← all JavaScript / jQuery logic
├── screenshots/        ← desktop.png, tablet.png, mobile.png
└── README.md           ← this file
```

## Design Notes
- Color scheme: deep navy/slate dark theme with blue accent (#4f7cff)
- Typography: Inter for UI, Fira Code for code blocks
- WCAG AA contrast compliant
- Tested at 320px – 1920px viewport widths
