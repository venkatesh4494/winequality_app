from get_data import read_params,get_data
import os
import argparse


def load_data(config_path):
    config=read_params(config_path)
    df=get_data(config_path)
    new_cols=[cols.replace(" ","_") for cols in df.columns]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path,sep=",",index=False,header=new_cols)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    df = load_data(config_path=parsed_args.config)

