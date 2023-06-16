import { useState } from 'react'
import './App.css'
import jobs from './jobs';

function App() {
  // We use the useState hook to manage the list of job summaries
  const [jobSummaries, setJobSummaries] = useState(jobs);


  // Function to handle the 'Not Interested' and 'Interested' button clicks
  // This simply removes the current job summary from the list
  const handleButtonClick = () => {
    setJobSummaries(jobSummaries.slice(1));
  };

  // Render the current job summary and the buttons
  return (
    <div>
      <h1>Job Swipe App</h1>
      {jobSummaries.length > 0 ? (
        <div>
          <p>{jobSummaries[0]}</p>
          <button onClick={handleButtonClick}>Not Interested</button>
          <button onClick={handleButtonClick}>Interested</button>
        </div>
      ) : (
        <p>No more jobs available!</p>
      )}
    </div>
  );
}

export default App
