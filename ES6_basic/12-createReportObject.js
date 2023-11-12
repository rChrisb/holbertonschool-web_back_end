export default function createReportObject(employeesList) {
  const getNumberOfDepartments = (employees) => Object.keys(employees).length;

  return {
    allEmployees: employeesList,
    getNumberOfDepartments,
  };
}
