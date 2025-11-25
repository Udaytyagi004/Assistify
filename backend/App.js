const express = require('express')
const axios = require('axios');

const app = express();

app.get("/" , (req , res) => {
  res.send("Hello from the server")
})
app.use(express.json())
// Example Express Route
app.post('/api/create-email', async (req, res) => {
  const { user_prompt } = req.body;
  
  try {
    // Call the Python Microservice
    const agentResponse = await axios.post('http://127.0.0.1:8000/generate-email', {
      user_id: "express_user",
      query: user_prompt
    });
    
    // Return the result to your frontend
    res.send(agentResponse.data);
    
  } catch (error) {
    res.status(500).json({ error: "Failed to generate email" });
  }
});

app.listen(3000, ()=> {
  console.log("server is up and running")
})