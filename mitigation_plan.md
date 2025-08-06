# Microservice A – Mitigation Plan

1. I implemented Microservice A for Aimee. It serves as the searchable database of video games.

2. The microservice is complete and fully functional.

    - It supports filtering by name, releaseYear, and genre using query parameters.

    - Responses are returned as JSON arrays.

    - It has been tested locally and with a sample frontend.

3. N/A — The microservice is complete.

4. How is your teammate going to access your microservice?

    - They can access the microservice in the following way:

        - Clone the code from GitHub:
        https://github.com/Binkersss/microservice_a

        - Run the microservice locally with (uv is required, install it with `pip install uv`):

            ```
            uv run uvicorn main:app --reload
            ```

    - The API will be available at:

        http://127.0.0.1:8000/games

    - The README.md contains the communication contract and example calls.

5. If you cannot access/call the microservice, you should:

    - Contact me via Discord or email and I’ll respond as quickly as possible.

    - I can help debug environment or CORS issues.

    - If absolutely necessary, I can temporarily host the service on Replit or Render for testing.

    - Availability:
    I’m available weekdays 9 AM – 7 PM PDT, and can be flexible for short support sessions outside of that window.

6. If you cannot access/call the microservice, please notify me of any issues by Friday, August 9, 2025, so I have time to help you before the final integration deadline.

7. Is there anything else your teammate needs to know?

    - CORS Note: If testing from a local HTML file, CORS must be enabled. I’ve already configured this in the server.

    - The database is currently loaded from games.json. If you want to swap it with your own data file, just make sure the schema is the same.

    - The microservice does not support POST/PUT/DELETE. It is read-only.
