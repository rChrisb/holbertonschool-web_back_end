export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // Simulate an API call or any asynchronous operation
    const isSuccess = Math.random() < 0.5; // For demonstration purposes

    // Resolve the promise if the operation is successful
    if (isSuccess) {
      const responseData = { message: 'API call successful' };
      resolve(responseData);
    } else {
      // Reject the promise if there is an error
      const error = new Error('API call failed');
      reject(error);
    }
  });
}
