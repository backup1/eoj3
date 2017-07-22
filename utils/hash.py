import hashlib


def case_hash(problem_id, case_input, case_output):
    hash1 = hashlib.sha256(problem_id).digest()
    hash2 = hashlib.sha256(case_input).digest()
    hash3 = hashlib.sha256(case_output).digest()
    return hashlib.sha256(hash1 + hash2 + hash3).hexdigest()


def file_hash(file):
    return hashlib.sha256(open(file, 'rb').read()).hexdigest()
