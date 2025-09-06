# GreenPay - Modern Banking Solutions Website

A modern, responsive website for GreenPay with Python Flask backend and intelligent chatbot functionality.

## Features

- **Responsive Design**: Mobile-first approach with modern UI/UX
- **Interactive Chatbot**: AI-powered chatbot with intelligent responses
- **Python Backend**: Flask-based REST API for chatbot and form handling
- **Modern Frontend**: Vanilla HTML, CSS, and JavaScript
- **Contact Forms**: Backend handling for contact submissions
- **Newsletter**: Subscription management system
- **Analytics**: Basic website statistics and health monitoring

## Tech Stack

### Frontend
- HTML5 with semantic markup
- CSS3 with custom properties and modern layouts
- Vanilla JavaScript with ES6+ features
- Responsive design with mobile-first approach

### Backend
- Python 3.8+
- Flask web framework
- Flask-CORS for cross-origin requests
- RESTful API design
- In-memory data storage (easily replaceable with database)

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask development server:**
   ```bash
   python app.py
   ```
   
   Or use the npm script:
   ```bash
   npm run dev-python
   ```

3. **The backend will be available at:**
   - Main website: http://localhost:5000
   - API endpoints: http://localhost:5000/api/*

### Frontend Development

For frontend-only development with Vite:
```bash
npm run dev
```

## API Endpoints

### Chatbot API
- **POST** `/api/chat`
  - Send messages to the chatbot
  - Returns intelligent responses with suggestions
  - Maintains conversation sessions

### Contact API
- **POST** `/api/contact`
  - Handle contact form submissions
  - Validates required fields
  - Stores submissions for follow-up

### Newsletter API
- **POST** `/api/newsletter`
  - Manage newsletter subscriptions
  - Prevents duplicate subscriptions
  - Returns confirmation messages

### Statistics API
- **GET** `/api/stats`
  - Website usage statistics
  - Chat session metrics
  - Business metrics display

### Health Check
- **GET** `/api/health`
  - System health monitoring
  - Uptime and version information

## Chatbot Features

The intelligent chatbot can handle various types of inquiries:

- **Greetings**: Welcome messages and conversation starters
- **Services**: Information about GreenPay's banking solutions
- **Payments**: Details about payment processing and methods
- **Account**: Help with account setup and management
- **Pricing**: Transparent pricing information and plans
- **Security**: Security features and compliance information
- **Contact**: Support contact information and channels
- **Help**: General assistance and guidance

### Chatbot Capabilities
- Context-aware responses
- Suggestion buttons for common follow-up questions
- Session management for conversation continuity
- Fallback responses for unrecognized queries
- Professional tone matching GreenPay's brand

## Project Structure

```
greenpay-website/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── index.html            # Main website HTML
├── style.css             # Stylesheet with modern design
├── script.js             # Frontend JavaScript functionality
├── package.json          # Node.js metadata and scripts
├── README.md             # Project documentation
└── logs/                 # Application logs (created automatically)
```

## Deployment

### Development
```bash
# Backend development
python app.py

# Frontend development (if using Vite)
npm run dev
```

### Production
For production deployment, consider:
- Using a production WSGI server like Gunicorn
- Setting up a reverse proxy with Nginx
- Using a proper database instead of in-memory storage
- Implementing proper logging and monitoring
- Setting up SSL certificates for HTTPS

Example production command:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Customization

### Adding New Chatbot Responses
Edit the `chatbot_responses` dictionary in `app.py` to add new keywords and response categories.

### Styling Changes
Modify `style.css` to customize the appearance. The design uses CSS custom properties for easy theme customization.

### Adding New API Endpoints
Follow the existing pattern in `app.py` to add new Flask routes and functionality.

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For technical support or questions:
- Email: support@greenpay.com
- Phone: +1 (555) 123-4567
- Documentation: This README file