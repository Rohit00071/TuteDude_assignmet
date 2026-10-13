const express = require("express");
const axios = require("axios");
const path = require("path");

const app = express();

const PORT = 3000;

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve frontend files
app.use(express.static(path.join(__dirname, "public")));

// Handle form submission
app.post("/submit", async (req, res) => {
    try {
        const { itemName, itemDescription } = req.body;

        const response = await axios.post(
            "http://backend:5000/submittodoitem",
            {
                itemName,
                itemDescription
            }
        );

        res.json(response.data);

    } catch (error) {
        console.error(error.message);

        res.status(500).json({
            error: "Unable to communicate with Flask backend"
        });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Frontend running on port ${PORT}`);
}); 