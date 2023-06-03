# Định nghĩa lớp Task
class Task:
    # Phương thức khởi tạo lớp Task
    def __init__(self, _pTask, _Delay, _Period):
        # Xác định biến pTask, Delay và Period của một tác vụ
        self.pTask = _pTask
        self.Delay = _Delay
        self.Period = _Period

    # Khai báo các thuộc tính của lớp Task
    pTask = None
    Delay = 0
    Period = 0
    RunMe = 0
    TaskID = -1

# Định nghĩa lớp Scheduler
class Scheduler:
    # Giá trị tick mặc định là 100ms
    TICK = 100
    # Số lượng tác vụ tối đa được lập lịch
    SCH_MAX_TASKS = 40
    # Danh sách các tác vụ được lập lịch
    SCH_tasks_G = []
    # Chỉ số hiện tại của tác vụ
    current_index_task = 0

    # Phương thức khởi tạo lớp Scheduler
    def __int__(self):
        return

    # Phương thức khởi tạo danh sách các tác vụ
    def SCH_Init(self):
        self.current_index_task = 0

    # Phương thức thêm một tác vụ mới vào danh sách các tác vụ để lập lịch chạy
    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            # Tạo một đối tượng Task mới với các thông số: hàm thực thi, khoảng thời gian trì hoãn và chu kỳ
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            # Gán chỉ số của tác vụ hiện tại cho TaskID
            aTask.TaskID = self.current_index_task
            # Thêm tác vụ mới vào danh sách các tác vụ và tăng chỉ số hiện tại lên 1 đơn vị
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
        else:
            # In ra thông báo nếu danh sách tác vụ đã đầy
            print("PrivateTasks are full!!!")

    # Phương thức cập nhật thông tin của danh sách các tác vụ
    def SCH_Update(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].Delay > 0:
                # Giảm giá trị khoảng thời gian trì hoãn đi 1 đơn vị nếu vẫn còn lớn hơn 0
                self.SCH_tasks_G[i].Delay -= 1
            else:
                # Đặt lại giá trị khoảng thời gian trì hoãn thành chu kỳ và tăng số lần thực thi lên 1
                self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
                self.SCH_tasks_G[i].RunMe += 1

    # Phương thức thực thi các tác vụ
    def SCH_Dispatch_Tasks(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].RunMe > 0:
                # Giảm số lần thực thi của tác vụ đi 1 đơn vị và gọi hàm thực thi tương ứng của tác vụ
                self.SCH_tasks_G[i].RunMe -= 1
                self.SCH_tasks_G[i].pTask()

    # Phương thức xóa một tác vụ khỏi danh sách các tác vụ
    def SCH_Delete(self, aTask):
        return

    # Phương thức tạo một ID duy nhất cho mỗi tác vụ
    def SCH_GenerateID(self):
        return -1
