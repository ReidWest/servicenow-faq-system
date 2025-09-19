# 🏢 ServiceNow Employee FAQ System

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional, ServiceNow-themed Employee FAQ web application built with Python Flask. Features intelligent keyword analysis, multi-topic search capabilities, and a responsive design that matches ServiceNow's brand identity.

## 📸 Screenshots

> **Note**: This is a local application. After installation, visit `http://localhost:8080` to see the live interface.

**Features Preview:**
- 🎨 ServiceNow-themed interface with professional branding
- 🔍 Intelligent search with natural language support  
- 📱 Responsive design that works on all devices
- 🏢 Multi-topic answers for complex questions

## ✨ Features

## Features

- **Clean Homepage**: Simple search interface with popular question shortcuts
- **Smart Search**: Keyword-based search through the knowledge base
- **Responsive Design**: Works great on desktop and mobile devices
- **Knowledge Base**: Pre-loaded with common employee questions and answers
- **Fallback Response**: AI-like placeholder response when no match is found
- **Professional Styling**: Modern, gradient-based design with smooth animations

## Knowledge Base Topics

The application can answer questions about:
- Password reset procedures
- W-2 forms and tax documents
- Vacation and sick leave policies
- Health insurance information
- 401(k) retirement plans
- Payroll and direct deposit
- Dress code guidelines
- Remote work policies
- Parking information
- IT support contact
- HR contact information

## 🚀 Quick Start

### Option 1: Clone and Run (Recommended)
```bash
# Clone the repository
git clone https://github.com/ReidWest/servicenow-faq-system.git
cd servicenow-faq-system

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Option 2: One-Click Setup
```bash
# Clone and install in one command
git clone https://github.com/ReidWest/servicenow-faq-system.git && cd servicenow-faq-system && pip install -r requirements.txt && python app.py
```

## 📋 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning)

### Detailed Setup Instructions

1. **Navigate to the project directory**:
   ```powershell
   cd employee_faq_app
   ```

2. **Create a virtual environment** (recommended):
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   ```powershell
   # On Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # On Windows (Command Prompt)
   venv\Scripts\activate.bat
   ```

4. **Install the required dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask development server**:
   ```powershell
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```
   or
   ```
   http://127.0.0.1:5000
   ```

3. **Use the application**:
   - Type questions in the search box
   - Click on popular question cards for quick access
   - Try searches like:
     - "password reset"
     - "vacation policy"
     - "W-2 forms"
     - "health insurance"
     - "IT support"

## Project Structure

```
employee_faq_app/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── templates/            # Jinja2 HTML templates
│   ├── base.html        # Base template with common layout
│   ├── index.html       # Homepage with search form
│   └── results.html     # Search results page
│
└── static/              # Static files
    └── css/
        └── style.css    # Application styles
```

## How It Works

1. **Search Process**: Users enter questions in the search form
2. **Keyword Matching**: The application searches the knowledge base using:
   - Exact phrase matching
   - Keyword-based search
   - Partial word matching
3. **Response Generation**: 
   - If a match is found, the corresponding answer is displayed
   - If no match is found, a helpful placeholder response is shown
4. **User Experience**: Clean interface with options to search again or try popular questions

## Customization

### Adding New FAQ Items

To add new questions and answers, edit the `KNOWLEDGE_BASE` dictionary in `app.py`:

```python
KNOWLEDGE_BASE = {
    "your new question": "Your detailed answer here...",
    # ... existing items
}
```

### Modifying the Placeholder Response

Update the placeholder response in the `search()` function in `app.py`:

```python
placeholder_response = ("Your custom message here...")
```

### Styling Changes

Modify `static/css/style.css` to change the appearance of the application.

## Technical Details

- **Framework**: Flask 2.3.3
- **Template Engine**: Jinja2
- **Styling**: Custom CSS with responsive design
- **Icons**: Font Awesome 6.0.0
- **Search Algorithm**: Keyword matching with fallback responses

## Troubleshooting

### Common Issues

1. **Port already in use**: If port 5000 is occupied, modify the port in `app.py`:
   ```python
   app.run(debug=True, host='127.0.0.1', port=5001)
   ```

2. **Module not found errors**: Ensure virtual environment is activated and dependencies are installed:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Template not found**: Make sure you're running the app from the correct directory where `app.py` is located.

### Development Mode

The application runs in debug mode by default, which provides:
- Auto-reload when files change
- Detailed error messages
- Interactive debugger

For production deployment, set `debug=False` in `app.py`.

## Future Enhancements

Potential improvements for the application:
- Database integration for dynamic FAQ management
- User authentication and role-based access
- Analytics and search logging
- Admin panel for content management
- Integration with ticketing systems (ServiceNow)
- Multi-language support
- Advanced search with synonyms and typo tolerance

## License

This project is created for internal employee use. Modify as needed for your organization.

## Support

For technical issues or questions about the application:
- Check the troubleshooting section above
- Review the Flask documentation: https://flask.palletsprojects.com/
- Contact your IT support team