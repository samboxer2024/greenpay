from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import json
import datetime
import os

app = Flask(__name__, static_folder='.', template_folder='.')
CORS(app)

# In-memory storage for demo purposes (use a database in production)
chat_sessions = {}
contact_submissions = []
newsletter_subscribers = []

# Chatbot responses database
chatbot_responses = {
    'greetings': [
        'hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'
    ],
    'services': [
        'service', 'services', 'what do you offer', 'features', 'products'
    ],
    'payment': [
        'payment', 'pay', 'transaction', 'money', 'transfer', 'billing'
    ],
    'account': [
        'account', 'profile', 'login', 'register', 'signup', 'sign up'
    ],
    'help': [
        'help', 'support', 'assistance', 'problem', 'issue', 'trouble'
    ],
    'pricing': [
        'price', 'pricing', 'cost', 'fee', 'charge', 'rate'
    ],
    'security': [
        'security', 'safe', 'secure', 'protection', 'privacy', 'encryption'
    ],
    'contact': [
        'contact', 'reach', 'phone', 'email', 'address', 'location'
    ]
}

def get_chatbot_response(message):
    """Generate appropriate chatbot response based on user message"""
    message_lower = message.lower()
    
    # Check for greetings
    if any(greeting in message_lower for greeting in chatbot_responses['greetings']):
        return {
            'message': 'Hello! Welcome to GreenPay. I\'m here to help you with any questions about our banking solutions. How can I assist you today?',
            'suggestions': ['Tell me about your services', 'How secure is GreenPay?', 'What are your pricing plans?']
        }
    
    # Check for services inquiry
    elif any(service in message_lower for service in chatbot_responses['services']):
        return {
            'message': 'GreenPay offers comprehensive banking solutions including:\n\n• Digital Payment Processing\n• Mobile Banking Applications\n• Secure Transaction Management\n• Real-time Analytics Dashboard\n• Multi-currency Support\n• API Integration\n\nWhich service would you like to know more about?',
            'suggestions': ['Digital Payments', 'Mobile Banking', 'Analytics Dashboard']
        }
    
    # Check for payment inquiries
    elif any(payment in message_lower for payment in chatbot_responses['payment']):
        return {
            'message': 'Our payment processing system supports:\n\n• Credit/Debit Cards (Visa, MasterCard, Amex)\n• Digital Wallets (PayPal, Apple Pay, Google Pay)\n• Bank Transfers\n• Cryptocurrency payments\n• International transactions\n\nAll payments are processed with bank-level security and real-time fraud detection.',
            'suggestions': ['Security features', 'Transaction fees', 'Integration help']
        }
    
    # Check for account inquiries
    elif any(account in message_lower for account in chatbot_responses['account']):
        return {
            'message': 'Getting started with GreenPay is easy!\n\n1. Create your merchant account (free signup)\n2. Complete identity verification\n3. Integrate our payment gateway\n4. Start accepting payments\n\nWould you like me to guide you through the registration process?',
            'suggestions': ['Start registration', 'Required documents', 'Integration guide']
        }
    
    # Check for pricing inquiries
    elif any(price in message_lower for price in chatbot_responses['pricing']):
        return {
            'message': 'GreenPay offers transparent, competitive pricing:\n\n• Starter Plan: 2.9% + $0.30 per transaction\n• Business Plan: 2.7% + $0.30 per transaction\n• Enterprise Plan: Custom rates for high volume\n\nNo setup fees, no monthly fees, no hidden charges. You only pay when you get paid!',
            'suggestions': ['Compare plans', 'Volume discounts', 'Contact sales']
        }
    
    # Check for security inquiries
    elif any(security in message_lower for security in chatbot_responses['security']):
        return {
            'message': 'Security is our top priority at GreenPay:\n\n• PCI DSS Level 1 Compliance\n• 256-bit SSL encryption\n• Two-factor authentication\n• Real-time fraud monitoring\n• Secure tokenization\n• Regular security audits\n\nYour data and transactions are protected with bank-level security.',
            'suggestions': ['Compliance certifications', 'Fraud protection', 'Data privacy']
        }
    
    # Check for contact inquiries
    elif any(contact in message_lower for contact in chatbot_responses['contact']):
        return {
            'message': 'You can reach our support team:\n\n📧 Email: support@greenpay.com\n📞 Phone: +1 (555) 123-4567\n💬 Live Chat: Available 24/7\n🌐 Help Center: help.greenpay.com\n\nOur team typically responds within 2 hours during business hours.',
            'suggestions': ['Schedule a call', 'Email support', 'Help center']
        }
    
    # Check for help requests
    elif any(help_word in message_lower for help_word in chatbot_responses['help']):
        return {
            'message': 'I\'m here to help! I can assist you with:\n\n• Account setup and verification\n• Payment processing questions\n• Technical integration support\n• Pricing and plan information\n• Security and compliance\n• General product questions\n\nWhat specific area do you need help with?',
            'suggestions': ['Account setup', 'Technical support', 'Billing questions']
        }
    
    # Thank you responses
    elif 'thank' in message_lower:
        return {
            'message': 'You\'re very welcome! I\'m glad I could help. Is there anything else you\'d like to know about GreenPay\'s services?',
            'suggestions': ['Learn more about services', 'Contact sales team', 'Start free trial']
        }
    
    # Goodbye responses
    elif any(bye in message_lower for bye in ['bye', 'goodbye', 'see you', 'thanks']):
        return {
            'message': 'Thank you for your interest in GreenPay! Have a great day, and don\'t hesitate to reach out if you have any more questions. We\'re here to help you succeed!',
            'suggestions': []
        }
    
    # Default response for unrecognized queries
    else:
        return {
            'message': f'I understand you\'re asking about "{message}". While I may not have specific information on that topic, our support team can provide detailed assistance. You can reach them at support@greenpay.com or +1 (555) 123-4567.',
            'suggestions': ['Contact support', 'Browse help center', 'Schedule a demo']
        }

@app.route('/')
def index():
    """Serve the main website"""
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    return send_from_directory('.', filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chatbot conversations"""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Initialize session if it doesn't exist
        if session_id not in chat_sessions:
            chat_sessions[session_id] = {
                'messages': [],
                'created_at': datetime.datetime.now().isoformat()
            }
        
        # Add user message to session
        chat_sessions[session_id]['messages'].append({
            'type': 'user',
            'message': message,
            'timestamp': datetime.datetime.now().isoformat()
        })
        
        # Generate bot response
        bot_response = get_chatbot_response(message)
        
        # Add bot response to session
        chat_sessions[session_id]['messages'].append({
            'type': 'bot',
            'message': bot_response['message'],
            'suggestions': bot_response.get('suggestions', []),
            'timestamp': datetime.datetime.now().isoformat()
        })
        
        return jsonify({
            'success': True,
            'response': bot_response['message'],
            'suggestions': bot_response.get('suggestions', []),
            'session_id': session_id
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field.title()} is required'}), 400
        
        # Store contact submission
        submission = {
            'id': len(contact_submissions) + 1,
            'name': data['name'],
            'email': data['email'],
            'phone': data.get('phone', ''),
            'company': data.get('company', ''),
            'message': data['message'],
            'submitted_at': datetime.datetime.now().isoformat(),
            'status': 'new'
        }
        
        contact_submissions.append(submission)
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! Our team will get back to you within 24 hours.',
            'submission_id': submission['id']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/newsletter', methods=['POST'])
def newsletter():
    """Handle newsletter subscriptions"""
    try:
        data = request.get_json()
        email = data.get('email', '').strip()
        
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        
        # Check if email already exists
        if any(sub['email'] == email for sub in newsletter_subscribers):
            return jsonify({'error': 'Email already subscribed'}), 400
        
        # Add to newsletter
        subscription = {
            'id': len(newsletter_subscribers) + 1,
            'email': email,
            'subscribed_at': datetime.datetime.now().isoformat(),
            'status': 'active'
        }
        
        newsletter_subscribers.append(subscription)
        
        return jsonify({
            'success': True,
            'message': 'Successfully subscribed to our newsletter!'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def stats():
    """Get website statistics"""
    return jsonify({
        'total_chat_sessions': len(chat_sessions),
        'total_messages': sum(len(session['messages']) for session in chat_sessions.values()),
        'contact_submissions': len(contact_submissions),
        'newsletter_subscribers': len(newsletter_subscribers),
        'uptime': '99.9%',
        'active_merchants': '10,000+',
        'total_processed': '$2B+'
    })

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)