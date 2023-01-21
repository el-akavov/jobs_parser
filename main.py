from headhunter import extract_max_page, extract_hh_jobs
from save import save_to_csv

hh_max_page = extract_max_page()
hh_jobs = extract_hh_jobs(hh_max_page)
save_to_csv(hh_jobs)