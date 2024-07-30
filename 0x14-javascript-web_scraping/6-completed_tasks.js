#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });

  const entries = Object.entries(completedTasks);
  const formattedOutput = entries.map(([key, value], index) => {
    if (index === 0) {
      return `{ '${key}': ${value}, `;
    } else if (index === entries.length - 1) {
      return ` '${key}': ${value} }`;
    } else {
      return ` '${key}': ${value},`;
    }
  }).join('\n');

  console.log(formattedOutput);
});
