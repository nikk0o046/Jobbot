import { useState } from 'react'
import './App.css'

function App() {
  const [jobSummaries, setJobSummaries] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [userHasSubmitted, setUserHasSubmitted] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setUserHasSubmitted(true);
    const inputString = event.target.elements.inputString.value;
    const response = await fetch('https://YOUR_BACKEND_FUNCTION_URL', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputString: inputString }),
    });
    const data = await response.json();
    setJobSummaries(data);
    setIsLoading(false);
  };

  const handleButtonClick = () => {
    setJobSummaries(jobSummaries.slice(1));
  };

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
      ) : userHasSubmitted ? (
        <p>No more jobs available!</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <label>
            Describe your background and the job you're looking for:
            <textarea id="inputString" name="inputString" />
          </label>
          <button type="submit">Submit</button>
        </form>
      )}
    </div>
  );
}

export default App;
