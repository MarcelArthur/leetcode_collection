# Write
# Solution Python
class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) / 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)

# C ++ 
class ExamRoom {
public:
    set<int> seats;
    int n;
    ExamRoom(int N) {
        // 保存一下N
        n = N;
    }

    int seat() {
        // 寻找座位
        int result = 0;
        if (seats.size() != 0) {
            result = 0;
            int idx = 0;
            int max_len = 0;
            // 查看0是否占用
            if (!seats.count(0)) {
                // 注意，最后的那个位置和0处的距离是不需要除2的
                max_len = *seats.begin() - 0;
                result = 0;
            }
            auto it = seats.begin(), end = seats.end();
            while (it != end) {
                int len = (*it - idx) / 2;
                if (len > max_len) {
                    max_len = len;
                    result = (*it + idx) / 2;
                }
                idx = *it;
                ++it;
            }
            // 看最后的位置有没有被占
            if (!seats.count(n - 1)) {
                int len = n - 1 - *seats.rbegin();
                if (len > max_len) {
                    max_len = len;
                    result = n - 1;
                }
            }
        }

        seats.insert(result);
        return result;
    }

    void leave(int p) {
        seats.erase(seats.find(p));
    }
};
/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */

