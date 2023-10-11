import re
from pathlib import Path

def extract_slha_and_info_from_banner(banner_path):
    """
    Extract the SLHA section, integrated weight, and number of events from a MadGraph banner.txt file.
    :param banner_path: Path to the banner file.
    :return: A tuple containing the SLHA content as a string, the integrated weight, and the number of events.
    """
    with banner_path.open('r') as f:
        content = f.read()
    # Extract SLHA
    slha_match = re.search(r'<slha>(.*?)<\/slha>', content, re.DOTALL)
    slha_content = slha_match.group(1).strip() if slha_match else None
    # Extract integrated weight
    weight_match = re.search(r'Integrated weight \(pb\)  :\s*(\d*\.\d+|\d+)', content)
    weight = float(weight_match.group(1)) if weight_match else None
    # Extract number of events
    events_match = re.search(r'Number of Events\s*:\s*(\d+)', content)
    num_events = int(events_match.group(1)) if events_match else None
    return slha_content, weight, num_events

def main():
    base_path = Path("/home/yoxara/MG5_aMC_v3_5_1/xsec_ppZp_CMS_Obs/Events/")
    banner_paths = [base_path / f"run_{i:02d}/run_{i:02d}_tag_1_banner.txt" for i in range(1, 32)]
    
    output_dir = Path("/home/yoxara/2MDM/Update_Data_val_SmodelS/ppZpjj/slhaFiles/xsec_ppZp_CMS_Obs")
    output_dir.mkdir(parents=True, exist_ok=True)

    for banner_path in banner_paths:
        if not banner_path.exists():
            print(f"Banner file {banner_path} does not exist. Skipping.")
            continue
        slha_content, weight, num_events = extract_slha_and_info_from_banner(banner_path)
        if all([slha_content, weight, num_events]):
            xsection_block = f"\nXSECTION  1.30E+04  2212 2212 1 5000001 # {num_events} events, [pb], pythia8 for LO\n 0  0  0  0  0  0   {weight} SModelS 3.0.0-beta"
            slha_content += xsection_block
            output_path = output_dir / banner_path.name.replace("_banner.txt", ".slha")
            with output_path.open('w') as f:
                f.write(slha_content)
            print(f"SLHA content with XSECTION saved to {output_path}")
        else:
            print(f"Failed to extract SLHA and/or weight and/or number of events from {banner_path}")

if __name__ == "__main__":
    main()