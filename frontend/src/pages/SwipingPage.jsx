import { useState } from 'react';

function SwipingPage() {
  const initialJobSummaries = ['Job 1', 'Job 2', 'Job 3']; // Predefined list of jobs
  const [jobSummaries, setJobSummaries] = useState(initialJobSummaries);

  const handleButtonClick = () => {
    setJobSummaries(jobSummaries.slice(1));
  };

  return (
    <div>
      <h1>Job Swipe Page</h1>
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

export default SwipingPage;

