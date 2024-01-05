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

def add_xsection_block(banner_path, output_dir, base_path_1, base_path_2):
    slha_content, weight, num_events = extract_slha_and_info_from_banner(banner_path)
    if all([slha_content, weight, num_events]):
        # Bloque de la sección transversal del primer base_path
        xsection_block = f"\nXSECTION  8.00E+03  2212 2212 1 9900032 # {num_events} events, [pb],  LO\n 0  0  0  0  0  303600   {weight} SModelS 3.0.0-beta"
        slha_content += xsection_block

        # Cambia el banner_path para el segundo base_path
        banner_path_2 = Path(str(banner_path).replace(str(base_path_1), str(base_path_2)))
        if banner_path_2.exists():
            _, weight_2, num_events_2 = extract_slha_and_info_from_banner(banner_path_2)
            if all([weight_2, num_events_2]):
                # Bloque de la sección transversal del segundo base_path con particle_id diferente
                xsection_block_2 = f"\nXSECTION  8.00E+03  2212 2212 1 9900026 # {num_events_2} events, [pb], noborn=QCD \n 0  0  0  0  0  303600   {weight_2} SModelS 3.0.0-beta"
                slha_content += xsection_block_2

        output_path = output_dir / banner_path.name.replace("_banner.txt", ".slha")
        with output_path.open('w') as f:
            f.write(slha_content)
        print(f"SLHA content with XSECTION saved to {output_path}")
    else:
        print(f"Failed to extract SLHA and/or weight and/or number of events from {banner_path}")

def main():
    base_path_1 = Path("/home/yoxara/MG5_aMC_v3_5_1/2mdm_zp_prod_2_random_8TeV_V2/Events")
    base_path_2 = Path("/home/yoxara/MG5_aMC_v3_5_1/2mdm_sd_prod_2_random_8TeV_V2/Events")
    banner_paths = list(base_path_1.glob("run_*/run_*_mzp_*_mchi_*_msd_*_banner.txt"))
    
    output_dir = Path("/home/yoxara/2MDM/slhaFiles_8TeV")
    output_dir.mkdir(parents=True, exist_ok=True)

    for banner_path in banner_paths:
        if not banner_path.exists():
            print(f"Banner file {banner_path} does not exist. Skipping.")
            continue
        add_xsection_block(banner_path, output_dir, base_path_1, base_path_2)

if __name__ == "__main__":
    main()