def get_download_url(file_url):
  data_url = 'https://drive.google.com/file/d/1BxCDGcoPO08q65NBLCSsJOeIGet-b4dR/view?usp=sharing'
  file_id = data_url.split('/')[-2]
  data_download_url = 'https://drive.google.com/uc?id=' + file_id

  return data_download_url