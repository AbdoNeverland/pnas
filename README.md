# PNAS (Phone Number Authentication System)

PNAS is a web application designed to provide developers with a RESTful API for phone number verification. Developers can sign up to use the API and integrate it into their applications to verify the authenticity of phone numbers provided by users.

## Features

- **Phone Number Verification**: Verify the authenticity of phone numbers provided by users.
- **RESTful API**: Easy-to-use API endpoints for integrating phone number verification into applications.
- **Developer Friendly**: Simple signup process for developers to start using the API.

## Getting Started

To get started with PNAS, follow these steps:

1. **Register**: go to pnas website, and create a new account (the website needs a valid phone number)

2. **Activate your account**: once registed, a verification code will be sent to your phone, enter the digits to activate your account

that's it, now you can use the pnas API


## API Documentation

This part provides detailed information on how to use the API endpoints for phone number verification.

## Base URL

The base URL for all API endpoints is:

```
https://.118.166.27
```

## Authentication

Authentication is required for accessing most of the API endpoints. Developers need to sign up and obtain an API key to authenticate requests.

## Endpoints: sending messages

- **Endpoint**: `/add-sms`
- **Method**: `POST`
- **Description**: send message to a specific phone number
- **Request Body**:

```json
{"email": "",
        "pwd": "your password",
        "phone": "your phone",
        "msg": "hello from pnas",
        "sendTo": "where to send message"
        }
```

- **Response**:

```json
{
  "msg": "sms was added to stack"
}
```

- **Error Response**:

```json
{
  "msg": "wrong user phone or password"
}
```


## Error Handling

In case of errors, the API will return appropriate HTTP status codes along with error messages in the response body.

---

## Contributing

We welcome contributions from the community! To contribute to PNAS, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'new feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
