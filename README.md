# Crypto API

## Overview
This application fetches cryptocurrency market updates from the CoinGecko API.

## Features
- List all coins.
- List coin categories.
- Get specific coin details by ID.
- Paginated responses.

## Setup

### Prerequisites
- Python 3.x
- Docker (optional, if you plan to use Docker)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gowthamsornala/cryptoMarket.git
   cd cryptoMarket

2. Create a virtual environment and activate it:
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the dependencies:
   pip install -r requirements.txt

4.Run the application:
   python run.py

### API Endpoints

Register new user:
POST   /api/v1/register

Generate token:
POST   /api/v1/login

List all coins:
GET   /api/coins?page_num=<page_num>&per_page=<per_page>

List all categories:
GET   /api/categories

Get coin details by ID:
GET   /api/coin/<coin_id>

## Authentication with JWT Token
### Register a New User: 
   To use the API, you need to register a new user.
   POST /api/v1/register
   #### Request Body:
   { "username": "john" }
   #### Response:
   { "message": "User registered successfully." }
### Login to Get Token: 
   After registering, log in to get a JWT token.
   POST /api/v1/login
   #### Request Body:
   { "username": "john" }
   #### Response:
   { "token": "your_jwt_token_here" }
### Use the Token: 
   Include the JWT token in the Authorization header when making requests to the protected endpoints.
   #### Example:
   GET /api/v1/coins
   #### Header:
   Authorization: Bearer your_jwt_token_here

## Docker
### Build the Docker Image
docker build -t app .

### Run the Docker Container
docker run -p 5000:5000 app

## Testing
### Run Unit Tests
python -m unittest discover -s tests

## Linting
### Run Linter
flake8 app

## Access the API documentation
Open your browser and navigate to http://localhost:5000/api/docs to view the Swagger UI for your API.



## Contributing

1. Fork the repository.

2. Create your feature branch.

3. Commit your changes.

4. Push to the branch.

5. Open a pull request.