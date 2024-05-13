
def sort_company():
    sorted_companies = sorted(company_detail_list.values(), key=lambda x: x['domain'], reverse=True)
    return [{'name': company['name'], 'domain': company['domain']} for company in sorted_companies]

def get_company_domain():
    for company_name, company_info in company_detail_list.items():
        domain = company_info['domain']
        num_clients = len(company_info['clients'])
        print(f"{company_name}: {domain}, relation: {num_clients} clients")

def get_employees():
    result = []
    for employee_name, employee_info in employee_detail_list.items():
        full_name = employee_info['full_name']
        company_name = employee_info['company']
        domain = company_detail_list[company_name]['domain']
        result.append({
            'full_name': full_name,
            'company': company_name,
            'domain': domain
        })
    return result

def get_employees_by_company():
    result = []
    for company_name, company_info in company_detail_list.items():
        employees = [employee for employee, emp_info in employee_detail_list.items() if emp_info['company'] == company_name]
        result.append({
            'company': company_name,
            'employees': employees
        })
    return result

# data
company_name_list = [{'name': 'Company 1'},
          {'name': 'Company 2'},
          {'name': 'Company 3'}]

employee_name_list = [{'name': 'John Doe'},
          {'name': 'Tom Smith'},
          {'name': 'Andrew Sebastian'}]

company_detail_list = {
      'Company 1': {
          'name': 'Company 1',
          'domain': 'Retail',
          'clients': [
              {
                  'name': 'acme.inc',
                  'country': 'united states'
              },
              {
                  'name': 'Wayne.co',
                  'country': 'united states'
              }
          ]
      },
      'Company 2': {
          'name': 'Company 2',
          'domain': 'Construction',
          'clients': [
              {
                  'name': 'Tesla',
                  'country': 'united states'
              },
              {
                  'name': 'Japan Airlines',
                  'country': 'japan'
              },
              {
                  'name': 'Indofood',
                  'country': 'indonesia'
              }
          ]
      },
      'Company 3': {
          'name': 'Company 3',
          'domain': 'Healthcare',
          'clients': [
              {
                  'name': 'Petronas',
                  'country': 'malaysia'
              },
              {
                  'name': 'VW Group',
                  'country': 'germany'
              },
              {
                  'name': 'IBM',
                  'country': 'united states'
              },
              {
                  'name': 'Mitsubishi',
                  'country': 'japan'
              }
          ]
      }
  }

employee_detail_list = {
      'John Doe': {
          'name': 'EMP-0001',
          'first_name': 'John',
          'last_name': 'Doe',
          'full_name': 'John Doe',
          'company': 'Company 1'
      },
      'Tom Smith': {
          'name': 'EMP-0002',
          'first_name': 'Tom',
          'last_name': 'Smith',
          'full_name': 'Tom Smith',
          'company': 'Company 2'
      },
      'Andrew Sebastian': {
          'name': 'EMP-0003',
          'first_name': 'Andrew',
          'last_name': 'Sebastian',
          'full_name': 'Andrew Sebastian',
          'company': 'Company 2'
      },
  }


# output no1 - 3
# no 1
resultNo1 = sort_company()
print("output soal no 1: ")
print(resultNo1)

# no 2
print("output soal no 2: ")
get_company_domain()

# no 3
resultNo3 = get_employees()
print("output soal no 3: ")
print(resultNo3)

# no 4
resultNo4 = get_employees_by_company()
print("output soal no 4: ")
print(resultNo4)