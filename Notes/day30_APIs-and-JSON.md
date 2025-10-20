### 🧩 **APIs (Application Programming Interfaces)**

-   **Definition:** A set of rules that allow software applications to communicate with each other.

-   **Types:**

    1.  **REST API** -- Uses HTTP requests (GET, POST, PUT, DELETE).

    2.  **SOAP API** -- Uses XML for communication.

    3.  **GraphQL API** -- Query-based; client specifies data needed.

-   **Common HTTP Methods:**

    -   **GET:** Retrieve data.

    -   **POST:** Send new data.

    -   **PUT:** Update existing data.

    -   **DELETE:** Remove data.

-   **Endpoint:** URL that gives access to specific data (e.g., `https://api.example.com/users`).

-   **Headers:** Send metadata like authorization tokens or content type.

-   **Response Codes:**

    -   `200 OK` -- Success

    -   `201 Created` -- Resource created

    -   `400 Bad Request` -- Invalid request

    -   `401 Unauthorized` -- No valid credentials

    -   `404 Not Found` -- Resource missing

    -   `500 Internal Server Error` -- Server failed

* * * * *

### 💾 **JSON (JavaScript Object Notation)**

-   **Definition:** A lightweight data format used to exchange data between systems.

-   **Syntax:** Key-value pairs inside `{}` with arrays `[]` for lists.

**Example:**

```
{
  "name": "Alice",
  "age": 25,
  "skills": ["Python", "JavaScript"],
  "active": true
}

```

-   **Data types:** string, number, boolean, array, object, null.

-   **Common Use:** APIs send/receive data in JSON format.

