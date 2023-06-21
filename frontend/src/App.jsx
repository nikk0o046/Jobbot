import { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  // We use the useState hook to manage the list of job summaries
  const [jobSummaries, setJobSummaries] = useState([]);
  const [userInput, setUserInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Function to handle the 'Not Interested' and 'Interested' button clicks
  // This simply removes the current job summary from the list
  const handleButtonClick = () => {
    setJobSummaries(jobSummaries.slice(1));
  };

  // Function to handle user input and send to the backend
  const handleUserInput = async (event) => {
    event.preventDefault();
    setIsLoading(true);

    const response = await axios.post('https://us-central1-grand-eye-390516.cloudfunctions.net/function-cors-test', {
      input_string: userInput
    });

    setJobSummaries(response.data);
    setIsLoading(false);
  };

  // Render the current job summary and the buttons
  return (
    <div>
      <h1>Job Swipe App</h1>
      {isLoading ? (
        <p>Processing...</p>
      ) : jobSummaries.length > 0 ? (
        <div>
          <p>{jobSummaries[0]}</p>
          <button onClick={handleButtonClick}>Not Interested</button>
          <button onClick={handleButtonClick}>Interested</button>
        </div>
      ) : (
        <div>
          <p>Describe your background and the job you're looking for:</p>
          <form onSubmit={handleUserInput}>
            <input value={userInput} onChange={e => setUserInput(e.target.value)} required />
            <button type="submit">Submit</button>
          </form>
        </div>
      )}
    </div>
  );
}

export default App;
