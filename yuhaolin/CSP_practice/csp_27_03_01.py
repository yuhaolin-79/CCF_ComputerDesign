import sys

def main():
    line1 = sys.stdin.readline().split()
    n = int(line1[0])
    
    # 风险地区 {id: [start_days]}
    risk_regions = {}
    # 漫游记录 [[receive_day, visit_day, user_id, region_id]]
    records = []
    
    def is_risk(r, day):
        """判断地区r在day日是否处于风险状态"""
        if r not in risk_regions:
            return False
        for d0 in risk_regions[r]:
            if d0 <= day <= d0 + 6:
                return True
        return False
    
    def check_continuous(r, d_start, d_end):
        """从访问日到今天都必须是风险状态"""
        for day in range(d_start, d_end + 1):
            if not is_risk(r, day):
                return False
        return True
    
    for d in range(n):
        data = sys.stdin.readline().split()
        r_cnt = int(data[0])
        m_cnt = int(data[1])
        
        # 风险地区
        for i in range(2, 2+r_cnt):
            p = int(data[i])
            if p not in risk_regions:
                risk_regions[p] = []
            risk_regions[p].append(d)
        
        # 当日漫游数据
        for _ in range(m_cnt):
            # d_visit,u,r
            m_data = sys.stdin.readline().split()
            dv, u, r = map(int, m_data)
            records.append([d, dv, u, r])
        
        risk_users = set()
        remained_records = []
        
        for rec in records:
            d_recv, d_visit, u_id, r_id = rec
            if d-7 < d_recv <= d:
                if d-7 < d_visit <= d:
                    if check_continuous(r_id, d_visit, d):
                        risk_users.add(u_id)
                
                remained_records.append(rec)
            else:
                pass
        records = remained_records
        
        if risk_users:
            res = sorted(list(risk_users))
            print(f"{d} {' '.join(map(str, res))}")
        else:
            print(d)

if __name__ == "__main__":
    main()