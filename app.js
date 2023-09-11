const express = require('express');
const app = express();
const port = process.env.PORT || 3000; // Use port 3000 if not specified

app.get('/api', (req, res) => {
  const slack_name = req.query.slack_name;
  const track = req.query.track;

  // Get the current day of the week
  const current_day = new Date().toLocaleString('en-US', { weekday: 'long' });

  // Get the current UTC time within a +/-2 minute window
  const now = new Date();
  const utc_time = new Date(now.getTime() + (now.getTimezoneOffset() * 60000) - (2 * 60 * 1000)).toISOString();

  // Constructing GitHub URLs based on my repository and file
  const github_repo_url = 'https://github.com/Abiodun001-world/zuriboard';
  const github_file_url = `${github_repo_url}/Abiodun001-world/master/app.js`;

  // Create the JSON response
  const response = {
    slack_name: slack_name,
    current_day: current_day,
    utc_time: utc_time,
    track: track,
    github_file_url: github_file_url,
    github_repo_url: github_repo_url,
    status_code: 200,
  };

  res.status(200).json(response);
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
