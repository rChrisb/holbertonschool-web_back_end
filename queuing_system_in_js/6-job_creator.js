import kue from "kue";
const push_notification_code = kue.createQueue({
  redis: {
    host: "localhost",
    port: "6479",
  },
});
const obj = {
  phoneNumber: "4153518780",
  message: "This is the code to verify your account",
};
const job = push_notification_code
  .create("push_notification_code", obj)
  .save((err) => {
    if (err) {
      console.log("Notification job failed", err);
    } else {
      console.log("Notification job created:", job.id);

      job.on("complete", () => {
        push_notification_code.shutdown()(500, (err) => {
          console.log("Kue shutdown:", err || "completed");
          process.exit(0);
        });
      });

      job.on("failed", () => {
        push_notification_code.shutdown()(500, (err) => {
          console.log("Kue shutdown:", err || "completed");
          process.exit(1);
        });
      });
    }
  });
