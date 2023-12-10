import redis from "redis";
const publisher = redis.createClient(6479);

publisher.on("connect", () => {
  console.log("Redis client connected");
});
publisher.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish("holberton school channel", message);
    // console.log(`${message} sent`);
    if (message === "KILL_SERVER") {
      process.exit(0);
      // publisher.quit();
    }
  }, time);
}

publishMessage("Holberton School #1 starts course", 100);
publishMessage("Holberton School #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton School #3 starts course", 400);
