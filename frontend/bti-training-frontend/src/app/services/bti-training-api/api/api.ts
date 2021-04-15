export * from './employee.service';
import { EmployeeService } from './employee.service';
export * from './root.service';
import { RootService } from './root.service';
export const APIS = [EmployeeService, RootService];
