import React, { useState, useContext } from "react";
import { AppContext } from "../AppProvider";
import { Container, TextField, Button, Typography } from "@mui/material";

const ProfilePage = () => {
  const { jobSummaries, setJobSummaries, setUserHasSubmitted } = useContext(AppContext);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setUserHasSubmitted(true); // Set userHasSubmitted to true on submit
    const inputString = event.target.elements.inputString.value;
    const response = await fetch('http://localhost:5000/function-jobbot', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input_string: inputString }),
    });
    const data = await response.json(); // It expects a jsonified list of job summaries
    setJobSummaries(data);
    setIsLoading(false);
  };

  return (
    <Container>
      {isLoading ? (
        <Typography>Analysing...</Typography>
      ) : jobSummaries?.length > 0 ? (
        <Typography>Analysis complete. Happy swiping!</Typography>
      ) : (
        <form onSubmit={handleSubmit}>
          <Typography variant="h6" gutterBottom>
            Briefly describe your education, experience and skills:
          </Typography>
          <TextField
            id="inputString"
            name="inputString"
            variant="outlined"
            fullWidth
            multiline
            rows={8}
            style={{ marginBottom: '1rem' }}
          />
          <Button type="submit" variant="contained" color="primary">
            Submit
          </Button>
        </form>
      )}
    </Container>
  );
}

export default ProfilePage;
