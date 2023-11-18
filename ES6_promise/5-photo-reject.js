export default function uploadPhoto(fileName) {
  return new Promise((resolve, reject) => {
    // Simulating an asynchronous operation, e.g., processing the photo
    setTimeout(() => {
      // For demonstration purposes, let's reject the promise with an error
      reject(new Error(`${fileName} cannot be processed`));
    }, 1000); // Simulating a delay of 1 second
  });
}
