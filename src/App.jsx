import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
   // Define the initial job summaries
   const initialJobs = [
    "Job 1: Software engineer at XYZ. Requires 3+ years of experience...",
    "Job 2: Data scientist at ABC. PhD in a related field preferred...",
    "Job 3: Web developer at JKL. Must know JavaScript and React...",
    "Job 4: Project manager at MNO. Certification in Project Management required...",
    "Job 5: Product manager at DEF. Previous experience in a tech company preferred..."
  ];

  // We use the useState hook to manage the list of job summaries
  const [jobs, setJobs] = useState(initialJobs);

  // Function to handle the 'Not Interested' and 'Interested' button clicks
  // This simply removes the current job summary from the list
  const handleButtonClick = () => {
    setJobs(jobs.slice(1));
  };

  // Render the current job summary and the buttons
  return (
    <div>
      <h1>Job Swipe App</h1>
      {jobs.length > 0 ? (
        <div>
          <p>{jobs[0]}</p>
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
