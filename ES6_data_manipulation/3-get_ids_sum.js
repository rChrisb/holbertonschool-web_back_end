export default function getStudentIdsSum(ids) {
  return ids.reduce((sum, student) => sum + student.id, 0);
}
